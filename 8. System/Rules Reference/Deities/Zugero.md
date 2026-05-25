---
type: deity
source-type: "Remaster"
domains: "Darkness, Indulgence, Knowledge, Repose"
favored-weapon: "Bola"
divine-font: "Harm"
divine-skill: "Acrobatics"
divine-spells: "Rank 1: [[Sleep]], Rank 2: [[Invisibility]], Rank 5: [[Illusory Scene]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Zugero encompasses both ends of the spectrum of battle. When she was a mortal, she was revered as a fantastic general; no other goblin had been said to emerge victorious in so many raids. Zugero considered there to be no need to enter a battle if there was no guaranteed victory. She planned out ambush points, having others create traps or use the environment to their favor. She kept her brilliant tactical mind sharp with constant rest. It wasn't uncommon for her soldiers to find her napping or drinking midengagement, nestled away safely behind back lines. According to tales, it was her most powerful nap ever that eventually elevated her to become the Dream Battler. She now appears as a goblin with pale green skin clad in slapdash armor made from scraps, carrying a number of armaments and trap devices around her belt. Depending on the observer, she either appears alert for battle or on the verge of falling asleep, which many goblins state is a sign as to which task the observer should focus on at the time.

**Title** The Dream Battler

**Areas of Concern** Ambushes, lurking, slacking

**Edicts** Fight today so you can rest tomorrow, work smart instead of hard, slack off and get away with it

**Anathema** Launch yourself thoughtlessly into work or combat

**Religious Symbol** cup on a pillow

**Sacred Animal** badger

**Sacred Colors** brown, black

**Source:** `= this.source` (`= this.source-type`)
