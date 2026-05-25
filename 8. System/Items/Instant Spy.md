---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Clockwork]]", "[[Consumable]]", "[[Gadget]]"]
price: "{'gp': 5}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

An instant spy is a tiny clockwork device that is small enough to be easily hidden. It contains the same audio-recording mechanisms as a clockwork spy, as well as a short-lived gemstone that can store up to 1 hour of sound to play back later.

Once you have activated the instant spy, it surreptitiously begins recording all the sounds around it for an hour. In general, it can hear sounds that are clearly audible in the location where you activated it, but not sounds that would require a Perception check with a DC of 10 or greater to hear. The GM determines exactly what the instant spy can hear and record, as well as whether or not the recording is clear in a situation where the original sound is quiet, distorted, or intentionally obscured.

When the recording is complete, once within the next 24 hours, you or another creature can use an Interact action to play back the stored audio in its entirety, after which the gem crumbles to dust. If no one plays the recorded sounds back within 1 day, the gem crumbles into dust anyway. This prevents the information from falling into the wrong hands later. It's typical to use the Conceal an Object action to hide an instant spy in a location once you've activated it, since if you don't hide it, it's relatively easy to discover in a thorough search, despite the fact that it's small and relatively unobtrusive.

**Source:** `= this.source` (`= this.source-type`)
