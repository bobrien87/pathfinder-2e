---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]"]
price: "{'gp': 4200}"
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

This vile poison is contagious, causing the victim's skin to secrete the toxin, allowing it to spread to others. While under the effects of choleric contagion, the first time during per round the victim succeeds at an attack roll with an unarmed attack against another creature, the target of the attack is exposed to the poison.

**Saving Throw** DC 40 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 6d10 poison damage (1 round)

**Stage 2** 8d10 poison damage (1 round)

**Stage 3** 10d10 poison damage (1 round)

**Source:** `= this.source` (`= this.source-type`)
