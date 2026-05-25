---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]", "[[Illusion]]", "[[Magical]]"]
price: "{'gp': 8}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Access** Member of a secret society

This parchment is crafted with illusion magic, allowing for the transfer of secret messages. You can fill the parchment with the usual amount of text, encoding your secret message within the innocuous message.

**Activate—Hide Message** 1 minute (manipulate)

**Effect** You tap the letters of your secret message one at a time, causing the letters to glow momentarily before fading to their standard ink color, and a symbol of your choice appears at the corner of the page. The next time someone taps the symbol with a writing instrument, the chosen letters glow again, revealing the secret message, and then the power of the parchment is spent.

**Source:** `= this.source` (`= this.source-type`)
