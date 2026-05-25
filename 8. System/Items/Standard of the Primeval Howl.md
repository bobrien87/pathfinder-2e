---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Magical]]", "[[Mental]]"]
price: "{'gp': 900}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These standards are always constructed from uncut wood and a leather banner painted with the visage of a snarling beast—a wolf, boar, bear, lion, dragon, or similarly imposing creature. And while it might become lost on a battlefield scattered with gaudier standards, its effect bolsters those around a competent leader. When carrying this banner, you gain a +1 item bonus to Intimidation checks and initiative rolls, and creatures in a @Template[type:emanation|distance:20] also gain a +1 item bonus to initiative checks.

**Activate** R (concentrate)

**Frequency** once per hour

**Trigger** An ally within 20 feet of you critically hits with a Strike

**Requirements** You have the [[Battle Cry]] skill feat

**Effect** You attempt to [[Demoralize]] the foe the Strike hit.

**Source:** `= this.source` (`= this.source-type`)
