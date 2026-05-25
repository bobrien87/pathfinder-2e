---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Morph]]", "[[Poison]]"]
price: "{'gp': 550}"
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

This substance is the result of a failed alchemical experiment to regrow a severed arm. An extra outsized, uncontrolled limb of the sort used for manipulation grows from the victim's body. The limb initially flails about, throwing the creature off-balance. Once it "matures," the limb pummels the victim instead. The limb can't deal its bludgeoning damage if the victim is unable to take actions. Upon recovery from the poison, the extra limb withers and falls off.

**Saving Throw** DC 32 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 4d6 poison damage, [[Clumsy]] 1, and must succeed at a DC 5 flat check to perform an action with the manipulate trait or the action fails and is lost (1 round)

**Stage 2** 4d6 poison damage, clumsy 1, [[Slowed]] 1, 2d6 bludgeoning damage (1 round)

**Stage 3** 4d6 poison damage, [[Clumsy]] 2, [[Slowed]] 2, 4d6 bludgeoning damage (1 round)

**Source:** `= this.source` (`= this.source-type`)
