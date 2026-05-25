---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "2"
cast: "1 day"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Many grow up and spend their lives eating with others, and doing so binds them—to their families, communities, and cultures. Food can form long-lasting bonds, and with a bit of extra work, those bonds can be shared.

You prepare a meal for a small gathering of up to 10 close friends, enough people to comfortably eat together at one table or in one circle. As you collect and prepare the food, you call upon spirits of home and memory. As they work through you and guide you, you perfectly recreate a dish that emotionally connects you to a place of your past: perhaps your mother's cooking when you were a child, or the way you and your comrades-in-arms cooked rations together when you fought in the war. When you're done, you share the meal and tell your new friends the story that comes with it. As they eat and drink, any participants of 4th level or lower sink into a snapshot of your past and can borrow insights from it for future use.
- **Critical Success** Your friends are vividly taken through your memories as you relive them, and they hold onto the experience even after the fugue ends. For the next week, they have a +4 circumstance bonus to Deception and Diplomacy checks to convince anyone from the community where the meal originated from that they are from that area or were present for events you described. Even after the raw magic infusing the memories fade, the memories don't, and your friends will be able to make the dish just as well as you can. Chances are, they like it just as much as you did.
- **Success** As critical success, except your friends get a +2 circumstance bonus to Deception and Diplomacy checks instead. They also can't make the meal themselves but probably look forward to tasting it the way you make it if you ever offer to cook it again.
- **Failure** Your friends see the vision as planned, but the magic doesn't quite take. As success, but no one receives any bonus. The real treasure will have to be the friends you fed along the way.
- **Critical Failure** Your friends see the vision as planned, and the magic takes hold—but it goes wrong, like a bad case of indigestion. The memories are scattered around the rest of their psyches, and it takes a week to settle down properly. They confuse parts of your past for theirs, and they take a –2 circumstance bonus to Deception and Diplomacy checks for the next week against anyone from your old community, as they confidently apply the wrong expectations from their lives across the one you were trying to introduce them to.

**Heightened (4th)** Participants up to 8th level can gain the benefits, and the cost is 40 gp.

**Heightened (6th)** Participants up to 12th level can gain the benefits, and the cost is 150 gp.

**Heightened (8th)** Participants up to 16th level can gain the benefits, and the cost is 480 gp.

**Heightened (10th)** Participants of any level can gain the benefits, and the cost is 2000 gp.

**Source:** `= this.source` (`= this.source-type`)
