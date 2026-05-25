---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Aquadynamic]]"]
price: "{'gp': 2000}"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+2 resilient coral armor*, often favored by allies of merfolk and aquatic elves, is made of living coral carefully harvested from the ocean depths. Legends speak of a variety of similar coral armors with distinct powers, but surface-dwellers know of *reef heart* as a magic armor that makes it easier for them to travel under the sea. *Reef heart* enables you to breathe underwater and gives you a swim Speed equal to half your land Speed.

**Activate** `pf2:3` (concentrate, manipulate)

**Frequency** once per day

**Effect** You cast [[Coral Eruption]]. If you conjure the coral underwater, it ceases dealing damage after 1 minute, but its duration is unlimited. If the magical coral remains in place for 1 year, it becomes non-magical coral from which a reef might grow.

**Source:** `= this.source` (`= this.source-type`)
