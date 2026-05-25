---
type: item
source-type: "Remaster"
level: "28"
traits: ["[[Artifact]]", "[[Deadly d8]]", "[[Divine]]", "[[Forceful]]", "[[Reach]]"]
price: "{'value': {}}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+4 major striking greater brilliant keen glaive* binds the souls of powerful creatures it slays. The soul can't be returned to life by any means while imprisoned within the glaive and can be freed only by a deed of great benevolence or selflessness. While using the glaive as a weapon, whenever you reduce a sapient creature of 18th level or higher to 0 Hit Points or roll a critical success with a Strike against such a target, the creature must attempt a DC 50 [[Fortitude]] save.
- **Critical Success** No additional effect.
- **Success** The glaive siphons the creature's essence, rendering it [[Drained]] 1. If the creature dies from the Strike or while drained in this way, the creature's soul is bound in the glaive.
- **Failure** As success, but the creature is [[Drained]] 2.
- **Critical Failure** As success, but the creature is [[Drained]] 4.

The glaive also has the following activations.

**Activate** `pf2:f` (concentrate)

**Trigger** You Strike with the Whisperer of Souls

**Effect** You choose whether the Strike deals lethal or nonlethal damage. If the glaive has a reason for doing so, such as slaying a creature whose soul the glaive can absorb, it can defy your choice if you fail a DC 50 [[Will]] save.

**Activate** `pf2:f` (concentrate)

**Trigger** You attempt an Occultism check to [[Decipher Writing]], [[Identify Magic]], [[Learn a Spell]], or [[Recall Knowledge]]

**Effect** You listen to eldritch secrets the weapon whispers, gaining a +4 item bonus to the triggering check.

**Activate** `pf2:3` (concentrate, manipulate)

**Frequency** once per week

**Effect** Attempt an Occultism check as if you cast the [[Collective Memories]] ritual about a subject. If you roll a success or critical success, you can repeat what the *Whisperer of Souls* relates to you about the subject. On a critical failure, you and the glaive are drawn into a murmuring void of cold, where your mind is assaulted by strange visions for an entire week. At the end of this time, you reappear and must attempt a DC 50 [[Will]] save.
- **Success** When you return, you can retrain one of your skills into a Lore skill about evil creatures or places, as if you had spent 1 week retraining.
- **Failure** As success, but you are [[Stupefied 2]] for 1 week.
- **Critical Failure** As success, but your alignment moves one step toward evil and you must retrain one of your skills into a Lore about evil creatures or places. You become obsessed with increasing your forbidden knowledge, turning to wicked forces that offer such secrets and compromising your morals further if you must.

**Destruction** If the *Whisperer of Souls* is used to slay Shelyn's herald, it disintegrates, bringing about great evil in its wake.

**Source:** `= this.source` (`= this.source-type`)
