---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "3"
cast: "2 hours"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Sometimes, the problems in your life are too oppressive. Sometimes, you have a case you need to crack and you have no idea where to start. When you've exhausted all options and willpower, you might as well just get drunk and call it a night. The butterfly bender is a ritual to kill two birds with one stone. By twisting fate around a session of hard drinking, you and a small party (no more than five people) suspend judgment, memory, and even consciousness as you all hurl yourselves into the arms of destiny and politely ask for a favor. You all get blackout drunk and, if all goes according to plan, you'll wake up with some progress upon a quest you've all undertaken—hopefully, without too much collateral damage.

The participants of the ritual wake up the next day with some of the following, determined by the results of the ritual. Any options that aren't chosen are temporarily lost to you.

- Your dignity.
- A common item that has the consumable trait of a level no higher than that of the ritual, which might be useful for an upcoming challenge. If lost, you misplace all of your currently carried items—including keys to where your equipment might be stored. With a modicum of effort, you recover your items within 1 day.
- A new friend or connection, as though you'd succeeded at a Diplomacy check to [[Make an Impression]] with a relevant NPC up to the ritual's level. If this is one of things lost, an existing friend refuses to speak to you for 1 day.
- A useful piece of information, as though you'd succeeded at a Diplomacy check to Gather Information. If lost, you take a –4 status penalty to your next check to Recall Knowledge.
- A convenient opportunity of the GM's choice. If there's no immediately relevant opportunity, you find an opportunity to [[Earn Income]] at the ritual's level + 1. If lost, the result of your next attempt to Earn Income is one degree of success worse.
- **Critical Success** Pick two options from the above list. The GM then gives you a bonus 3rd option of their choice.
- **Success** Pick two options from the above list.
- **Failure** Pick one option from the above list.
- **Critical Failure** Pick two options from the above list. The GM gives you one of them.

**Source:** `= this.source` (`= this.source-type`)
