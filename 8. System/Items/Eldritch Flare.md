---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]"]
price: "{'gp': 1100}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

This poison draws power from the magic of its victim. If a creature under the effects of eldritch flare Casts a Spell, excess magical energy feeds back into the toxin, increasing the DC of the poison by 2 that round. In addition, if the spell deals damage, the poison deals half its damage as one of the types of damage the spell deals (the other half remains poison damage). If the target is immune or has resistance to the spell's damage, the poison deals half its damage as mental damage instead. If the victim casts no spells during a round while affected, the poison still deals its poison damage.

**Saving Throw** DC 35 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 8d6 untyped damage (1 round)

**Stage 2** 10d6 untyped damage (1 round)

**Stage 3** 12d6 untyped damage (1 round)

**Source:** `= this.source` (`= this.source-type`)
