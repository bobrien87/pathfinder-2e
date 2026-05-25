---
type: creature
group: ["Aberration"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Quelaunt"
level: "15"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Aberration"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+29; [[Tremorsense]] (imprecise) 60 feet"
languages: "Aklo ((Can't Speak Any Language), Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Deception +30, Intimidation +30, Occultism +27"
abilityMods: ["+6", "+5", "+4", "+5", "+6", "+8"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Emotional Focus"
    desc: "The quelaunt can cast the following cleric domain spells as 8th-rank occult innate spells at will without spending Focus Points: [[Captivating Adoration]], [[Delusional Pride]], and [[Ignite Ambition]]."
armorclass:
  - name: AC
    desc: "36; **Fort** +27, **Ref** +26, **Will** +31"
health:
  - name: HP
    desc: "305; **Resistances** mental 15"
abilities_mid:
  - name: "+2 to Will Saves vs. Emotion"
    desc: ""
  - name: "Spiral of Despair"
    desc: "`pf2:0` **Trigger** A creature fails a saving throw to resist one of the quelaunt's innate spells or emotional focus spells <br>  <br> **Effect** As the quelaunt invades the triggering creature's mind and plants the seeds of negative emotions, it also strips away the target's feelings of hope or positivity. The quelaunt can immediately end a single emotion effect from which the triggering creature is benefiting."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +30 (`pf2:1`) (agile, magical, reach 10 ft., unarmed), **Damage** 3d8+12 slashing"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 39, attack +31<br>**5th** [[Wave of Despair]]<br>**4th** [[Fly]] (Constant)<br>**2nd** [[Laughing Fit]]<br>**1st** [[Fear]] (At Will)"
  - name: "Emotional Focus"
    desc: "DC 39, attack +31<br>**4th** [[Captivating Adoration]], [[Delusional Pride]]<br>**1st** [[Ignite Ambition]]"
abilities_bot:
  - name: "Emotional Frenzy"
    desc: "`pf2:3` The quelaunt casts up to three spells chosen from its at-will innate spells and its emotional focus spells."
  - name: "Feed on Emotion"
    desc: "`pf2:1` **Frequency** once per round; <br>  <br> **Effect** The quelaunt feeds on the emotional unrest of a single creature within 30 feet that's under a harmful emotion effect. The target must succeed at a DC 37 [[Will]] save or take 4d10 mental damage and be [[Stunned]] for 1 round. <br>  <br> If the target fails its saving throw, the quelaunt regains the same number of Hit Points and regains the action it spent to Feed on Emotion. It can't use the regained action to Feed on Emotion again."
  - name: "Rapid Strikes"
    desc: "`pf2:2` The quelaunt makes three melee Strikes, each against a different target within reach. The multiple attack penalty applies to each attack but increases only after all the attacks have been made."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

This three-armed, three-legged monster has no discernible eyes, nose, ears, or mouth, and no visible means of ingesting food. Its limbs are distributed so evenly across its body that it's all but impossible to tell which way the creature is oriented at any given time. Few who witness a quelaunt linger on its alien looks for long though, as the invasion of their minds becomes a more pressing concern, sowing doubt, sorrow, and rage. This monstrosity not only delights in the negative emotions of its prey, but feeds on them, gaining strength and sustenance from their dismay. For the quelaunt, no act is too terrible or cruel to inflict on its victims, since the more a creature suffers, the more the quelaunt feasts.

Quelaunts are known to associate with other aberrant horrors, including jah-tohls and other creatures associated with the Dominion of the Black. However, the more prevalent theory paints them as more alien—perhaps invasive beings from another dimension of pure thought and feeling—and claims that in their natural state they have no physical bodies at all. Few dare speculate further; the only known autopsy of a quelaunt resulted in the researcher's suicide just days afterward and all the notes were mysteriously destroyed. Whatever secrets there are to be unlocked in the anatomy of these bizarre monsters are apparently important enough to warrant great protection from quelaunts, even after death.

```statblock
creature: "Quelaunt"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
