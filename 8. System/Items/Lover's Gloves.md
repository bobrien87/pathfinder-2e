---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Emotion]]", "[[Invested]]", "[[Magical]]", "[[Mental]]"]
price: "{'gp': 500}"
usage: "worngloves"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These white silk gloves are adorned in red hearts that glow faintly whenever you are adjacent to someone you feel particularly strongly toward. They buoy your spirit, giving you a +1 item bonus to Diplomacy checks.

**Activate—Bond** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** You grasp the hands of a willing creature you have strong positive feelings about, regardless of the nature of those feelings. The creature gains a +1 status bonus to saving throws and 10 temporary Hit Points for 10 minutes. If the creature shares your feelings, you gain the same benefits, and for the duration, when you both roll a success on a saving throw against an emotion effect that causes negative emotions, you both get a critical success instead.

> [!danger] Effect: Lover's Gloves

**Source:** `= this.source` (`= this.source-type`)
