---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Injury]]", "[[Poison]]"]
price: "{'gp': 80}"
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

Derived from a mixture of krooth venom and an agitating agent, scarlet mist causes bleeding that turns into a foaming mist. When a creature under the effects of scarlet mist takes persistent bleed damage from the toxin, creatures within 5 feet take the splash damage. The persistent damage can't be staunched until the poison's effects end. A creature that can't bleed doesn't take the bleed damage or cause the splash damage but can still take the poison damage.

**Saving Throw** DC 25 [[Fortitude]] save

**Maximum Duration** 6 rounds

**Stage 1** 3d6 poison damage, 1d4 persistent,bleed damage, and 1 poison splash damage (1 round)

**Stage 2** 3d6 poison damage, 2d4 persistent,bleed damage, and 2 poison splash damage (1 round)

**Stage 3** 3d6 poison damage, 3d4 persistent,bleed damage, and 3 poison splash damage (1 round)

**Source:** `= this.source` (`= this.source-type`)
