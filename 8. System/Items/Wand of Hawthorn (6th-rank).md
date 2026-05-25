---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Magical]]", "[[Plant]]", "[[Wand]]"]
price: "{'gp': 4500}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Carved from a hawthorn branch, this wand has a smooth handle, but the shaft remains covered in bark and long thorns. Polished red stones, arranged like a cluster of berries, decorate the pommel.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast 6th-rank [[Oaken Resilience]], and the target sprouts long thorns like those of a hawthorn tree. While [[Oaken Resilience]] lasts, any creature that hits the target with an unarmed Strike or otherwise touches it takes 3d4 piercing damage from the thorns. A creature that has engulfed or swallowed the target takes this damage as well at the start of each of the target's turns.

**Craft Requirements** Supply a casting of *oaken resilience* of the appropriate rank.

**Source:** `= this.source` (`= this.source-type`)
