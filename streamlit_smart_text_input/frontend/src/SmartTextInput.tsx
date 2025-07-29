import React, { ReactNode, useEffect } from "react";
import Select from "react-select";
import {
  ComponentProps,
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection
} from "streamlit-component-lib";
import SmartTextInputStyle from "./styling";

const LoadGoogleFont = () => {
  useEffect(() => {
    const link = document.createElement("link");
    link.href = "https://fonts.googleapis.com/css2?family=Source+Sans+Pro&display=swap";
    link.rel = "stylesheet";
    document.head.appendChild(link);
  }, []);

  return null;
};

interface State {
  isFocused: boolean;
  extended: boolean;
  selectedOption: OptionType | null;
  inputOption: String | null;
  rawInput?: string;
}

interface OptionType {
  label: String | null;
  value: String | null;
  userInput: boolean | null;
}

class SmartTextInput extends StreamlitComponentBase<State> {
  private style = new SmartTextInputStyle(this.props.theme!);

  constructor(props: ComponentProps) {
    super(props);
    const options = this._getOptionsFromArgs();
    this.state = {
      isFocused: false,
      extended: false,
      selectedOption: (props.args.index !== null) ? options[props.args.index] : null,
      inputOption: null,
      rawInput: ""
    };
    if (this.state.selectedOption) {
      this._updateComponent(this.state.selectedOption);
    }

    this._handleOnChange = this._handleOnChange.bind(this);
    this._updateComponent = this._updateComponent.bind(this);
    this._updateInputOption = this._updateInputOption.bind(this);
    this._debounce = this._debounce.bind(this);
  }

  public render = (): ReactNode => {
    return (
      <>
        <LoadGoogleFont />
        <div
          style={{
            ...this.style.wrapper,
            cursor: this.props.args.disabled ? "not-allowed" : "default",
          }}
        >
          {this.props.args.label_visibility !== "collapsed" && (
            <div style={{ visibility: this.props.args.label_visibility }}>
              <label style={this.style.getLabelStyle(this.props.args.disabled)}>
                {this.props.args.label}
              </label>
            </div>
          )}
          <Select
            id={this.props.args.key ? this.props.args.key : "free-text-selectbox"}
            value={this.state.selectedOption}
            placeholder={this.props.args.placeholder}
            options={this._getOptions()}
            styles={this.style.select}
            components={{
              ClearIndicator: (props) => this.style.clearIndicator(props),
              DropdownIndicator: () => this.style.iconDropdown(this.state.extended, this.props.args.disabled),
              IndicatorSeparator: () => <div></div>,
            }}
            inputValue={this.state.rawInput}
            onInputChange={(value, { action }) => {
              if (action === "input-change") {
                this.setState({ rawInput: value });
              }
            }}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                const val = this.state.rawInput?.trim();
                if (val) {
                  const option: OptionType = { label: val, value: val, userInput: true };
                  this._updateComponent(option);
                  this._updateInputOption(option);
                  this.setState({ selectedOption: option, rawInput: "" });
                }
              }
            }}
            onChange={(event: any) => { this._handleOnChange(event); }}
            isClearable={true}
            isSearchable={true}
            onMenuOpen={() => this.setState({ extended: true })}
            onMenuClose={() => this.setState({ extended: false })}
            menuIsOpen={this.state.extended}
            isDisabled={this.props.args.disabled}
            menuPlacement="auto"
          />
        </div>
      </>
    );
  };

  private _getOptionsFromArgs(): OptionType[] {
    return this.props.args.options.map((option: string) => {
      return { label: option, value: option, userInput: false };
    });
  }

  private _getOptions(): OptionType[] {
    let options = this._getOptionsFromArgs();
    if (
      !options.some(option => option.value === this.state.selectedOption?.value)
      && !this.state.selectedOption?.userInput
      && this.state.selectedOption?.value !== null
    ) {
      this._handleOnChange(null);
    }
    if (this.state.inputOption !== null) {
      options.unshift({ label: this.state.inputOption, value: this.state.inputOption, userInput: true });
    }
    return options;
  }

  private _handleOnChange(option: OptionType | null): void {
    if (option === null) {
      if (this.state.selectedOption !== null) {
        option = { label: null, value: null, userInput: false };
        this._updateInputOption(option);
        this.setState({ selectedOption: null });
        this._updateComponent(option);
      }
    } else {
      this._updateComponent(option);
      this.setState({ selectedOption: option });
    }
  }

  private _updateComponent(option: OptionType): void {
    if (option.value === null || option.value === "" || option.value === undefined) {
      Streamlit.setComponentValue(null);
    } else {
      Streamlit.setComponentValue(option.value);
    }
  }

  private _updateInputOption(option: OptionType): void {
    if (option.value === null || option.value === "" || option.value === undefined) {
      this.setState({ inputOption: null });
    } else {
      this.setState({ inputOption: option.value });
    }
  }

  private _debounce(func: (...args: any[]) => void, timeout: number = 300) {
    let timer: ReturnType<typeof setTimeout>;
    return (...args: any[]) => {
      clearTimeout(timer);
      timer = setTimeout(() => { func.apply(this, args); }, timeout);
    };
  }
}

export default withStreamlitConnection(SmartTextInput);
