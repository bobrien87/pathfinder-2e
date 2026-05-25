---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Light]]", "[[Magical]]", "[[Mental]]"]
price: "{'gp': 50}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This hooded lantern takes the form of a translucent prism. It functions as a normal Hooded Lantern, except that it isn't fueled by oil, but by oaths. While you're holding the lantern, you gain a +1 item bonus to Diplomacy checks.

**Activate—Announce Oath** `pf2:r` (light, mental)

**Trigger** You make a promise in good faith

**Effect** The *oathlamp of accord* sheds light without consuming fuel until the promise you made is broken or fulfilled. The GM adjudicates whether a spoken promise is broken or fulfilled. This light and the shutters to conceal it work as normal for a hooded lantern. Any creature in the light of the oathlamp becomes aware of the contents of the oath, along with who made it and how long ago.

**Source:** `= this.source` (`= this.source-type`)
