---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Magical]]", "[[Scrying]]"]
price: "{'gp': 3800}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This polished crystal sphere enhances scrying magic. Any visual information received through a spell with the scrying trait that was cast by the *crystal ball* appears within the sphere, and any auditory information sounds out from the surface of the sphere. When you cast a spell with the scrying trait by any other means while holding the sphere, you can relay any information you receive in the same way, allowing others to see or hear the target.

The base version of a crystal ball is a sphere of clear quartz, but other versions are made of different stones.

**Activate—Clairvoyance** 1 minute (concentrate, manipulate)

**Frequency** once per hour

**Effect** The *crystal ball* casts [[Clairvoyance]] to your specifications.

**Activate—Scrying** 10 minutes (concentrate, manipulate)

**Frequency** twice per day

**Effect** The *crystal ball* casts a DC 33 [[Will]] save [[Scrying]] spell to your specifications.

**Source:** `= this.source` (`= this.source-type`)
