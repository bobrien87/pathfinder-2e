---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Magical]]", "[[Thrown 20]]", "[[Water]]"]
price: "{'gp': 4000}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Colorful stripes and trailing ribbons give this *+2 greater striking underwater wounding spear* an appearance like a poisonous lionfish. While holding the spear, you gain a +2 item bonus to Athletic checks to [[Swim]].

Strikes with this weapon deal an additional 1d6 poison damage.

**Activate—Lionfish Poison** R (concentrate)

**Frequency** once per hour

**Trigger** You successfully Strike a creature with the *lionfish spear*

**Effect** The spear injects lionfish poison into the target

**Saving Throw** DC 31 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 3d6 poison damage and [[Sickened]] 1 (1 round)

**Stage 2** 5d6 poison damage and [[Sickened]] 2 (1 round)

**Stage 3** [[Paralyzed]] for 2d4 hours

**Source:** `= this.source` (`= this.source-type`)
