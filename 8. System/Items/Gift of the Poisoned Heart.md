---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Consumable]]", "[[Cursed]]", "[[Magical]]", "[[Unholy]]"]
price: "{'per': 1, 'value': {}}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** 1 minute (concentrate, manipulate)

Those who fail to see the curse view this object as a priceless gift, capable of restoring life to the deceased, but deep in the heart of this diamond lies a single flaw: a fissured occlusion of sickly, tainted red. To activate the diamond, place it on the relatively intact body of a creature that died within the past year. The stone shatters, restoring the recipient to life with the effects of a successful [[Resurrect]] ritual, except there's no limit to the level of the creature that can be revived.

This gift of life comes with a terrible cost: the recipient believes you—and anyone else who aided in the resurrection—deliberately caused their death and revived them only in furtherance of some nefarious scheme. Having a proxy activate the *gift of the poisoned heart* is of no use, as the item's magic sniffs out all coconspirators and uses your attempt to avoid the drawback to feed the resurrected creature's paranoia.

No amount of information or persuasion can alleviate this mistrust, as the cursed creature twists the facts endlessly to fit their delusion. Only magic such as [[Cleanse Affliction]] can neutralize this effect, and the subject resists any attempt to alter their beliefs by magic.

**Source:** `= this.source` (`= this.source-type`)
