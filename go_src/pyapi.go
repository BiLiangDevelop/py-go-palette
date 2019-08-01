package main

import (
	"C"
	"encoding/base64"
	"github.com/generaltso/vibrant"
	"image/png"
	"strings"
)

//export CalcPalette
func CalcPalette(pngImgBase64 *C.char, maxColorCount int) *C.char {
	checkErr := func(err error) {
		if err != nil {
			panic(err)
		}
	}

	pngImgBase64Str := C.GoString(pngImgBase64)

	reader := base64.NewDecoder(base64.StdEncoding, strings.NewReader(pngImgBase64Str))

	img, err := png.Decode(reader)
	checkErr(err)

	palette, err := vibrant.NewPalette(img, maxColorCount)
	checkErr(err)

	result := ""
	for name, swatch := range palette.ExtractAwesome() {
		result += name + "\t" + swatch.String() + "\n"
	}

	// return cgo string
	cStr := C.CString(result)

	return cStr
}

func main() {
}
