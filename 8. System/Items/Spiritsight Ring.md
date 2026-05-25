---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 225}"
usage: "worn"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The opal set in this intricately carved ivory ring eventually becomes translucent and tickles your finger whenever an incorporeal creature is nearby. When in the presence of a nearby incorporeal creature, even if it's within a solid object, you eventually detect the creature, though you might not do so instantly, and you can't pinpoint the location. This acts as a vague sense, similar to humans' sense of smell. An incorporeal creature trying to hide its presence from this sense attempts a Stealth check against your Perception DC to hide from your vague sense, as normal for attempting to foil special senses. You gain a +2 item bonus when using the [[Seek]] action to find [[Hidden]] or [[Undetected]] incorporeal creatures within 30 feet of you.

**Source:** `= this.source` (`= this.source-type`)
