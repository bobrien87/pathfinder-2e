---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Expandable]]"]
price: "{'gp': 45}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

The dried, shrunken corpse of a giant tarantula inside this smoked glass bottle is obscured by swirling vapor and cobwebs. You can throw the ampoule up to 30 feet when you Activate it. When you open or throw the ampoule, a Large giant tarantula effigy bursts forth and lunges at one adjacent creature. If the target fails a DC 21 [[Fortitude]] save, it takes @Damage[(1d10+4)[piercing]] damage. If the target critically fails the save, it's also exposed to tarantula venom.

**Giant Tarantula Venom** (poison)

**Saving Throw** DC 23 [[Fortitude]] save

**Maximum Duration** 8 rounds

**Stage 1** 1d10 poison damage (1 round)

**Stage 2** 1d12 poison damage, [[Clumsy]] 1, and [[Off Guard]] (1 round)

**Stage 3** 2d6 poison damage, [[Clumsy]] 2, and off-guard (1 round)

**Stage 4** 2d6 poison damage and [[Paralyzed]] (1 round)

**Craft Requirements** Supply the corpse of a giant tarantula.

**Source:** `= this.source` (`= this.source-type`)
