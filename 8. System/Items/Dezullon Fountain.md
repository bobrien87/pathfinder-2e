---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Acid]]", "[[Agile]]", "[[Plant]]", "[[Repeating]]"]
price: "{'gp': 1300}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *dezullon fountain* is a distinct type of *+2 striking air repeater* made from the still-living pitcher of a dezullon, dealing acid damage instead of the gun's normal piercing damage.

**Activate** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** The next creature you successfully Strike with this weapon is exposed to amnesia venom.

**Amnesia Venom** (mental, poison)

**Saving Throw** DC 29 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** [[Off Guard]] (1 round)

**Stage 2** off-guard and [[Clumsy]] 1 (1 round)

**Stage 3** [[Confused]], off-guard, and [[Clumsy]] 2 (1 round)

**Craft Requirements** The initial raw materials must include a pitcher from a dezullon or similar creature.

**Source:** `= this.source` (`= this.source-type`)
