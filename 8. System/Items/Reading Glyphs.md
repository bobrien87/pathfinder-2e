---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 90}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These tattoos on your knuckles look like strange glyphs in an unknown language. If you press your fingertips to text in any language, these glyphs cycle in appearance through those of various extant languages. Encrypted text causes your glyphs to turn to a recognizable "null" symbol.

**Activate** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** You sync the tattoos with the text your fingertips are touching. By running your fingers across the text, you translate it, with glyphs on your knuckles showing the translation in a language you can read. Your tattooed glyphs can't translate encrypted or encoded text, language couched in metaphor, and the like, subject to GM discretion.

**Source:** `= this.source` (`= this.source-type`)
