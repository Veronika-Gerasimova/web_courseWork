import { type PropType } from 'vue';
import { type BarcodeFormat } from 'barcode-detector/pure';
declare const _default: import("vue").DefineComponent<{
    formats: {
        type: PropType<BarcodeFormat[]>;
        default: () => BarcodeFormat[];
    };
}, {}, unknown, {}, {}, import("vue").ComponentOptionsMixin, import("vue").ComponentOptionsMixin, {
    detect: (...args: any[]) => void;
}, string, import("vue").VNodeProps & import("vue").AllowedComponentProps & import("vue").ComponentCustomProps, Readonly<import("vue").ExtractPropTypes<{
    formats: {
        type: PropType<BarcodeFormat[]>;
        default: () => BarcodeFormat[];
    };
}>> & {
    onDetect?: (...args: any[]) => any;
}, {
    formats: ("aztec" | "code_128" | "code_39" | "code_93" | "codabar" | "databar" | "databar_expanded" | "data_matrix" | "dx_film_edge" | "ean_13" | "ean_8" | "itf" | "maxi_code" | "micro_qr_code" | "pdf417" | "qr_code" | "rm_qr_code" | "upc_a" | "upc_e" | "linear_codes" | "matrix_codes" | "unknown")[];
}, {}>;
export default _default;
