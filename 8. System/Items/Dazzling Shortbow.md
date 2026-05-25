---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Deadly d10]]", "[[Magical]]"]
price: "{'gp': 160}"
usage: "held-in-one-plus-hands"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 striking shortbow* is a favorite of mage hunters and those who frequently fight enemies who can turn themselves [[Invisible]]. A creature who is critically hit with a ranged Strike from a *dazzling shortbow* must succeed at a DC 19 [[Fortitude]] save or be [[Dazzled]] for 1 minute.

**Activate—Show Yourself!** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** You fire an arrow that glows with purple light at a spot. Each creature in a @Template[type:burst|distance:10] within 60 feet is affected by [[Revealing Light]] (DC 19).

**Craft Requirements** Supply one casting of *revealing light*.

**Source:** `= this.source` (`= this.source-type`)
