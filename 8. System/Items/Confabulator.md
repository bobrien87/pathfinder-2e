---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Illusion]]", "[[Magical]]"]
price: "{'gp': 55}"
usage: "affixed-to-instrument"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This device attaches to any non-percussive musical instrument, allowing a non-verbal character to shape the sounds of the instrument into speech. The speech can be any language the character understands, and the sound of the speech resembles the instrument the device is attached to. You also gain a +1 item bonus to Performance checks made with the instrument.

**Source:** `= this.source` (`= this.source-type`)
