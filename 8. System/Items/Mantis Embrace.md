---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 700}"
usage: "worngloves"
bulk: "L"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These stylized red gloves are constructed from plates of leather that have been treated to resemble insect chitin. The gloves grant the wearer a +2 item bonus to Athletics checks to [[Grapple]] or [[Shove]].

**Activate—Crushing Embrace** `pf2:1` (manipulate)

**Frequency** once per hour

**Requirements** You are grappling a creature

**Effect** You Strike the creature you are grappling with a melee weapon or unarmed attack. This Strike deals an additional 3d6 precision damage and gains the death trait. The body of a creature that is slain by Crushing Embrace is so gruesomely damaged that the creature's body cannot be affected by any effect that requires an intact body to function, such as the [[Talking Corpse]] spell.

**Source:** `= this.source` (`= this.source-type`)
