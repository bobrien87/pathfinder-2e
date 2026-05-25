---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Invested]]", "[[Occult]]", "[[Scrying]]", "[[Unholy]]"]
price: "{'value': {}}"
usage: "other"
bulk: "2"
source: "Pathfinder NPC Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This magic mirror is the conduit between the mirror seer and the source of their power. Any creature who looks in this silver mirror can speak with the entity the mirror is linked to, but only a creature who has made a pact with the entity can activate the *malefic mirror*. If the mirror is shattered, any spells created by the mirror end (it has AC 5, object immunities, Hardness 5, HP 20, and BT 10).

**Activate—Peer Beyond** 10 minutes (concentrate, occult)

**Effect** The mirror casts a DC 28 [[Scrying]] spell for the benefit of the creature activating it. The target must be within the owner's domain (typically within 20 miles of the mirror). The viewer's familiarity with the target doesn't affect the spell's DC.

**Activate—Mirror Mimicry** 10 minutes (concentrate, manipulate, occult)

**Effect** The mirror transforms its owner's appearance into an exact copy of any humanoid the owner desires, with a pale mimicry of that creature's abilities. This has the effects of a 3rd-rank [[Illusory Disguise]] spell with a duration of 4 hours. The activation can also be Dismissed.

In addition, the disguised creature can automatically create illusions to mimic the abilities of the subject, with the appearance of spells, abilities, or even impressive physical deeds. These deeds are entirely illusory and can be disbelieved with a successful DC 28 [[Perception]] check. If an illusion makes it appear as though the creature moved farther or differently than they actually can (such as making them fly or teleport), the actual creature turns [[Invisible]], and their illusory image persists until the end of the creature's next turn. If the creature and their illusory self aren't in the same space at that point, the activation ends, revealing the deception.

**Source:** `= this.source` (`= this.source-type`)
