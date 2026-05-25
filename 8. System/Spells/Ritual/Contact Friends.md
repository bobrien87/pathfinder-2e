---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "3"
cast: "1 hour"
duration: "up to 10 minutes"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You meditate for a quiet moment before your mind seeks out others whom you have befriended, as well as friends of any of the secondary casters. The ritual projects your mind to a blank space where you see one or more friends from your past. Once there, you can ask each friend a single question. If more than one friend is present, you can ask each one a different question. These friends aren't compelled to answer you honestly or answer at all, but those who are your friends are likely to help you if they can, barring special situations.
- **Critical Success** You contact up to three close friends of yourself or any of the secondary casters, and the friends attempt to help you with their knowledge. They each answer one of your questions, as described above.
- **Success** As critical success, but your mind reaches one friend, instead of three.
- **Failure** Your mind reaches three friends you've made in the past, but each of them gives you a useless fact. None of these facts help with your situation at all.
- **Critical Failure** Your mind freezes. You saw something that terrified you to your core, leaving you and all other casters [[Stupefied 3]] for 1 day.

**Source:** `= this.source` (`= this.source-type`)
