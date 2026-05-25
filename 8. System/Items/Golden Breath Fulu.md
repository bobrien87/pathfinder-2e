---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Consumable]]", "[[Fulu]]", "[[Healing]]", "[[Magical]]", "[[Talisman]]", "[[Vitality]]"]
price: "{'gp': 8100}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You take damage.

An enterprising chirurgeon reversed the forces evoked by a *void thousand-pains fulu* to create the *golden breath fulu*, which fortifies qi and the body as elements move out of balance. When you Activate this fulu, you regain 75 healing Hit Points and attempt a flat check to end any persistent damage affecting you. The fulu is particularly appropriate help for ending any persistent damage. Also, if you would regain more Hit Points from the fulu than your maximum, you can gain the excess as temporary Hit Points or distribute the excess among creatures of your choice within 30 feet. The temporary Hit Points last for 1 minute.

> [!danger] Effect: Golden Breath Fulu

**Source:** `= this.source` (`= this.source-type`)
