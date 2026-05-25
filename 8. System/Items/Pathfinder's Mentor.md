---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Illusion]]", "[[Intelligent]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 200}"
usage: "worn"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Perception** +15; precise vision 30 feet, imprecise hearing 30 feet

**Communication** telepathy (Common and two other common languages)

**Skills** Pathfinder Lore +15, Society +13, Survival +13

**Int** +3, **Wis** +3, **Cha** +1

**Will** +14

A *Pathfinder's mentor* is a wayfinder that has developed sapience. It has two *aeon stone* slots, and both stones grant their resonant powers without interfering with each other. If both slots are filled, the *wayfinder* and two stones count as two items toward your investiture limit. Most Pathfinder's mentors are eager explorers that object to staying in one location for long, urging their bearers toward ancient ruins to explore, relics to study, and discoveries to make. To this end, the wayfinder acts as a guide, making Survival checks on your behalf during your travels. A *Pathfinder's mentor* also has the following activations.

**Activate** `pf2:1` (concentrate)

**Effect** The wayfinder casts [[Know the Way]] on you.

**Activate** 1 minute (concentrate, manipulate)

**Frequency** once per day

**Effect** The wayfinder casts [[Wanderer's Guide]] on you.

**Source:** `= this.source` (`= this.source-type`)
