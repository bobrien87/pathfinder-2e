---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]"]
price: "{'gp': 60}"
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

Smother shroud robs a victim of distinguishing features, making it difficult for anyone to identify the corpse. Swelling and distention of facial features makes the victim unrecognizable. Increase the DC of any checks made to identify a creature under the effects of smother shroud by twice the stage of the poison. If the victim dies while under the effects of this poison, its corpse retains an inability to take actions with the auditory trait, and if it tries to speak and fails, it counts against responses to the talking corpse spell.

**Saving Throw** DC 22 [[Fortitude]] save

**Maximum Duration** 10 rounds

**Stage 1** 2d4 poison damage and [[Dazzled]] (1 round)

**Stage 2** 3d4 poison damage, dazzled, a –4 status penalty to Perception checks to hear and smell, and must succeed at a DC 10 flat check to take actions with the auditory trait or the action is lost (1 round)

**Stage 3** 4d4 poison damage, [[Blinded]], [[Deafened]], unable to smell, unable to take actions with the auditory trait, and unable to breathe

**Source:** `= this.source` (`= this.source-type`)
