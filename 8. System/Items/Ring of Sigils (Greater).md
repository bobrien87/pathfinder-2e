---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Arcane]]", "[[Invested]]"]
price: "{'gp': 225}"
usage: "worn"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This silver band is carved with the personal sigils of different individuals, adding one to represent you when you invest it. The ring allows you to cast [[Sigil]] as an arcane innate cantrip.

**Activate—Track Sigil** `pf2:1` (concentrate, detection)

**Frequency** once per 10 minutes

**Effect** You detect the general direction toward the most recent *sigil* you created using the ring. This activation fails if the *sigil* is more than 100 miles away or if there's lead or running water between you and the *sigil*. In addition, if the *sigil* was placed on a living creature, you also determine whether the creature is alive, its distance from you, and any conditions affecting it.

**Source:** `= this.source` (`= this.source-type`)
