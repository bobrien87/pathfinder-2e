---
type: creature
group: ["Construct", "Earth"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Golem"
level: "8"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Construct"
trait_02: "Earth"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16"
languages: "Common (can't speak any language)"
skills:
  - name: Skills
    desc: "Athletics +20, Religion +18"
abilityMods: ["+6", "+2", "+5", "+1", "+4", "+0"]
abilities_top:
  - name: "At-Will Spells"
    desc: "The monster can cast its at-will spells any number of times without using up spell slots."
  - name: "Consecrated Fists"
    desc: "After the golem casts a holy spell, their Strikes deal an additional 1d8 spirit damage and gain the divine and holy traits. These benefits last until the end of the golem's next turn."
armorclass:
  - name: AC
    desc: "25; **Fort** +19, **Ref** +12, **Will** +16"
health:
  - name: HP
    desc: "170; **Immunities** acid"
abilities_mid:
  - name: "Day of Rest"
    desc: "A golem needs 1 day of rest per week or it becomes uncontrollable. An uncontrollable golem is unable to cast spells, and it takes a –2 circumstance penalty to checks made using Wisdom, including Will saves. While uncontrollable, the golem loses its immunity to sleep. The golem is uncontrollable until it takes a day of rest."
  - name: "Faithful"
    desc: "A golem faithfully serves its creator as long as it's not in an uncontrollable state (see above). While the golem is faithful, it follows the commands of its creator, even to its own detriment. While the golem remains faithful to its creator, the golem can't be [[Confused]] or [[Controlled]] by any creature other than its creator."
  - name: "Hefty Helper"
    desc: "The golem can carry 13 Bulk before becoming [[Encumbered]] and can carry a maximum Bulk of 18."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +20 (`pf2:1`) (reach 10 ft.), **Damage** 2d10+8 bludgeoning plus [[Consecrated Fists]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 24, attack +16<br>**4th** [[Divine Wrath]]<br>**3rd** [[Holy Light]] (At Will)<br>**2nd** [[Calm]], [[Dispel Magic]]<br>**1st** [[Divine Lance]], [[Heal]], [[Stabilize]]"
abilities_bot:
  - name: "Rampage"
    desc: "`pf2:2` **Requirements** The golem is uncontrollable <br>  <br> **Effect** The golem makes a melee Strike against every creature in its reach, whether that creature is an ally or not. The attacks count toward its multiple attack penalty normally, but the penalty does not increase until after all the Strikes are complete."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Long ago, the priests of ancient religions mastered a technique to bring them closer to their god: the animation of clay into a living being. These clay beings, called golems, are animated by placing a piece of paper with the name of the priest's god within the golem's mouth (or, in some cases, by carving a holy word on the golem's forehead). Though they are intelligent as a result of their divine blessing, golems generally don't act unless commanded to, and they rarely have the capacity for speech, a gift the gods bestowed on their creations alone. Instead, they use their intelligence to facilitate their maker's communion with their god in divine rites unknown outside of a religion's most faithful.

In some oppressed communities, golems serve as protectors against outside violence, fighting as a last resort but aiming to defuse situations first. Other times, the golem operates as a guardian to a temple or helper to a holy person. In rare cases, golems have been known to go on rampages when they aren't allowed a day of rest every week. These rampages can be extremely destructive to the communities the golems otherwise protect, so makers must endeavor to take good care of their creations.

Golem legends are diverse and widespread across the Inner Sea region and beyond. Some tell of even stranger powers bestowed on the golem, such as the ability to summon the spirits of the dead. Golems with such abilities are undoubtedly created by the most holy of priests, attuned to their god beyond what most mortals could hope to accomplish.

```statblock
creature: "Golem"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
