---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Contact]]", "[[Poison]]", "[[Virulent]]"]
price: "{'gp': 350}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:3` (manipulate)

This oily, dark-purple powder gives off the distinct odor of boiled leather. When delivered, the poison acts quickly to constrict the victim's blood flow to their extremities and turn their lungs into a soft jelly. A victim of astringent venom is recognizable by the frostbite-like hue of their hands as they lose circulation to their extremities, making it difficult for them to hold things. Each round at the beginning of their turn, a creature affected by astringent venom must succeed at a DC 5 flat check or drop one random item they're holding.

**Saving Throw** DC 32 [[Fortitude]] save

**Onset** 1 round

**Maximum Duration** 6 rounds

**Stage 1** 6d6 poison damage (1 round)

**Stage 2** 8d6 poison damage (1 round)

**Stage 3** 10d6 poison damage and [[Confused]] (1 round)

**Source:** `= this.source` (`= this.source-type`)
