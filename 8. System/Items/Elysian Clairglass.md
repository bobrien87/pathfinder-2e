---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Magical]]", "[[Scrying]]"]
price: "{'gp': 14000}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Used by soldiers who battle on the borderlands of Elysium, particularly in Gorum's realm of Clashing Shore, these bronze spyglasses are somewhat plain-looking save for a single diamond set into the largest cylinder. An *Elysian clairglass* functions like a typical spyglass, but you can see twenty times farther while looking through it, rather than eight times farther. It also grants a +3 item bonus to Perception checks to notice details at a distance.

**Activate—Seek and Speak** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** The *Elysian clairglass* casts clairaudience and clairvoyance on the area you are currently observing with it. As long as you're holding the *Elysian clairglass*, you can speak through the floating eye or ear created by its spells, causing your voice to manifest as a whisper that only one person in range of the spells can hear, as a booming voice that everyone in range of the spells can hear, or as any combination in between those two extremes.

**Activate—Pinpoint** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You cast [[Pinpoint]].

**Source:** `= this.source` (`= this.source-type`)
