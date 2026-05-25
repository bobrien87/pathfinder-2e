---
type: deity
source-type: "Remaster"
domains: "Confidence, Freedom, Pain, Protection"
favored-weapon: "Rapier"
divine-font: "Harm, Heal"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Endure]], Rank 2: [[Animus Mine]], Rank 5: [[Never Mind]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Arazni's transformation from mortal to true god has tested the bounds of the possible. As a mortal, she fought unceasingly to better the lives of her Arcadian compatriots. She so impressed the god Aroden that, after her untimely death, he elevated her to be his herald, the Red Crusader, and she continued to fight for humanity. Yet in 3823 ar, the Knights of Ozem fatefully chose to bind her to their will as they rallied against the Whispering Tyrant. Despite her heroism in leading the charge, the Whispering Tyrant prevailed, and he took particular delight in capturing, humiliating, torturing, and finally killing her. Although the Knights of Ozem recovered her body, they—and Aroden—failed her again when the necromancer Geb had her body stolen and then reanimated against her will, turning her into a lich. In thrall to Geb for over a thousand years, she ruled his nation, all the while suffering torments that changed her profoundly. She endured all of them.

Not long ago, Arazni decided to risk allying with mortals once again and, with their help, succeeded in tricking the Whispering Tyrant into destroying the magic that bound her to lichdom and to Geb. During her time on Geb's throne, she had been worshipped as a god, though few of the Gebbite masses who paid her obeisance were sincere. Arazni dismissed most of her true believers as sycophants, but for those trapped by unwilling bonds and other believers beyond Geb's borders, Arazni was a paragon of resilience and determination that reflected their own fierce struggles. Perhaps owing to their devotion, ending her lichdom didn't end her. She reemerged not just as a demigod, but as a full-fledged deity resplendent with power.

**Title** The Unyielding

**Areas of Concern** the abused, dignity, unwilling undeath

**Edicts** act with dignity, do whatever it takes to survive, despise and never forgive those who have hurt you

**Anathema** create unwilling undead, insult Arazni

**Religious Symbol** winged rapier

**Sacred Animal** red fox

**Sacred Colors** crimson, gray

**Source:** `= this.source` (`= this.source-type`)
