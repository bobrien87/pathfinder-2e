---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]"]
price: "{'gp': 13000}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Access** member of the Red Mantis assassins

**Activate** `pf2:2` (manipulate)

Kept as a closely guarded secret by the deadly members of the Red Mantis assassins, this poison is treated with reverence for its ability to end lives. If the victim dies while affected by this poison, its body decomposes to nothing in 1 minute, leaving only its gear behind. Non-magical preservation can't protect the tainted corpse. [[Peaceful Rest]] works on the poisoned body only if cast as a 5th-rank spell and the caster succeeds at a counteract check against the poison's saving throw DC when casting the spell. Even if cast successfully, *peaceful rest* only works as if it had been cast at 2nd rank.

**Saving Throw** DC 42 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 7d12 poison damage and [[Doomed]] 1 (1 round)

**Stage 2** 9d12 poison damage and [[Doomed]] 2 (1 round)

**Stage 3** 11d12 poison damage and [[Doomed]] 3 (1 round)

**Source:** `= this.source` (`= this.source-type`)
