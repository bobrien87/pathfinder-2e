---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Agile]]", "[[Apex]]", "[[Finesse]]", "[[Invested]]", "[[Magical]]", "[[Nonlethal]]", "[[Unarmed]]"]
price: "{'gp': 80000}"
usage: "worngloves"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These silken handwraps feature intricate embroidery of a serpentine red dragon adorned with golden thread. The handwraps function as +3 major striking greater flaming handwraps of mighty blows. You also gain a +4 item bonus to Athletics checks made to [[Grapple]] or [[Shove]]. When you invest the handwraps, you either increase your Strength modifier by 1 or increase it to +4, whichever would give you a higher value.

**Activate** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** You slap the bottom of your palms with hands splayed outward, casting a 7th-rank [[Breathe Fire]] spell ([[Reflex]] save).

**Activate** `pf2:f` (concentrate)

**Frequency** once per hour

**Trigger** You succeed or critically succeed with a Grapple

**Effect** You gain a +2 status bonus to your Athletics DC against any checks made to [[Escape]] your grapple until the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
