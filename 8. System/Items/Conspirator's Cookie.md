---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 15}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

The shape and exact flavor of these chocolate-covered cookies vary slightly based on who prepares them and the language they are imbued with when crafted. Although named for their use in obfuscating communications, Diarra finds them useful for quite the opposite reason.

After eating one of these treats, you can speak and understand the chosen language for the next hour. If you have the Read Lips or Sign Language feat, you can use that language with those feats. A conspirator's cookie grants you a +1 item bonus to Diplomacy checks to [[Make an Impression]] or [[Request]] in the chosen language and you can add your level even if untrained.

**Craft Requirements** You must know the chosen language.

**Source:** `= this.source` (`= this.source-type`)
