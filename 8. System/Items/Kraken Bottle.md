---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Expandable]]"]
price: "{'gp': 5000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

Coiled tentacles make it all but impossible to see anything else inside this ampoule. When opened, a Gargantuan kraken bursts forth, which can appear in water instead of on the ground. Its arms attempt to grasp up to four creatures with a reach of 60 feet. The kraken repositions [[Grabbed]] creatures to a different space within its reach unless the target succeeds at a DC 38 [[Fortitude]] save.

If the kraken is in water, it then releases a cloud of ink in an @Template[emanation|distance:80]. This cloud has no effect outside of water. Creatures inside the cloud are undetected, can't use their sense of smell, and are exposed to kraken ink poison. The cloud dissipates after 1 minute.

Krakens are immune to this poison.

**Saving Throw** DC 39 [[Fortitude]] save

**Maximum Duration** 10 rounds

**Stage 1** 4d6 poison damage and [[Sickened]] 1 (1 round)

**Stage 2** 5d6 poison damage and [[Sickened]] 2 (1 round)

**Craft Requirements** Supply the corpse of a kraken.

**Source:** `= this.source` (`= this.source-type`)
