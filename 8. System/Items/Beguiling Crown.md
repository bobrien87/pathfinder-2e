---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Apex]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 80000}"
usage: "wornheadwear"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This hugely massive crown is bedazzled with glimmering jewels and enchanted with powerful magics that make the gold seem to ripple and surge like strange glimmering tide pools. While uncomfortable to wear, the crown beguiles those within the wearer's presence. Creatures within 30 feet of you automatically improve their attitude toward you by one step (up to friendly). This doesn't prevent hostile creatures from attacking you, but it might give you a chance to talk to them before they strike. The dazzling nature of the crown makes it hard for you to read the intentions of others, and you take a –4 status penalty to your Perception DC when someone uses Deception against you. When you invest the crown, you either increase your Charisma modifier by 1 or increase it to +4, whichever would give you a higher value.

**Activate** `pf2:1` (concentrate)

**Frequency** once per round

**Effect** You're the subject of the [[Sanctuary]] spell until the end of your next turn.

**Activate** R (concentrate)

**Frequency** once per hour

**Trigger** A creature succeeds at an attack roll against you

**Effect** The creature must succeed at a DC 41 [[Will]] save or the attack roll becomes a failure and the target is friendly to you until the end of its turn. On a critical failure, the target becomes friendly to you, drops to their knees, and begs your forgiveness for 1 minute or until another creature takes a hostile action against them.

**Activate** `pf2:2` (concentrate, fortune, mental)

**Frequency** once per day

**Effect** Choose one living creature within 30 feet of you. That creature must succeed at a DC 41 [[Will]] save saving throw or become helpful to you for the next 24 hours. If they succeed, they become friendly to you for 1 hour. If they critically succeed they're immune to this effect for 1 year.

**Source:** `= this.source` (`= this.source-type`)
