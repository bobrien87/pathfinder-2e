---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Agile]]", "[[Finesse]]", "[[Magical]]", "[[Poison]]", "[[Thrown 10]]", "[[Versatile s]]"]
price: "{'gp': 150}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The serrated blade of this *+1 striking dagger* has a greenish tinge, and the hilt is sculpted to look like the head of a serpent about to strike.

When you critically succeed at an attack roll with the *serpent dagger*, the target becomes [[Sickened]] 1 unless it succeeds at a DC 19 [[Fortitude]] save. This is a poison effect.

In addition, you can activate the dagger to poison a creature with a more potent poison.

**Activate—Drip Poison** `pf2:f` (manipulate)

**Frequency** once per day

**Trigger** You damage a creature with the *serpent dagger*

**Effect** You poison the creature you hit with dagger venom.

**Dagger Venom** (poison)

**Saving Throw** DC 21 [[Fortitude]] save

**Maximum Duration** 4 rounds

**Stage 1** 1d8 poison damage and [[Enfeebled]] 1

**Source:** `= this.source` (`= this.source-type`)
