---
type: creature
group: ["Humanoid", "Mutant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Aapoph Serpentfolk"
level: "3"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Mutant"
trait_03: "Serpentfolk"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: "Aklo, Sakvroth (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +7, Athletics +11, Intimidation +6"
abilityMods: ["+4", "+2", "+3", "-1", "+1", "-1"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Serpentfolk Venom"
    desc: "**Saving Throw** DC 20 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d4 poison damage and [[Enfeebled]] 1 (1 round) <br>  <br> **Stage 2** 2d4 poison damage and enfeebled 1 (1 round)"
armorclass:
  - name: AC
    desc: "18; **Fort** +10, **Ref** +7, **Will** +6"
health:
  - name: HP
    desc: "60; **Resistances** poison 5"
abilities_mid:
  - name: "+2 Status to Will Saves vs. Mental"
    desc: ""
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Scimitar +11 (`pf2:1`) (forceful, sweep), **Damage** 1d6+6 slashing"
  - name: "Melee strike"
    desc: "Fangs +11 (`pf2:1`), **Damage** 1d8+6 piercing plus [[Serpentfolk Venom]]"
  - name: "Melee strike"
    desc: "Tail +11 (`pf2:1`) (agile), **Damage** 1d6+6 bludgeoning plus [[Knockdown]]"
spellcasting: []
abilities_bot:
  - name: "Slithering Attack"
    desc: "`pf2:1` The aapoph serpentfolk makes one scimitar or fangs Strike and one tail Strike, each targeting a different creature. These attacks both count toward the aapoph's multiple attack penalty, but the penalty doesn't increase until after the aapoph makes both attacks."
  - name: "Knockdown"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Aapophs possess greater strength and stronger venom than their zyss kin, but they lack zyss's innate magic. Unlike their selfish superiors, aapophs are communal and group together to hunt, wrestle, and sleep curled together in pits.

Aapophs often have physical mutations—horns, vestigial tails, or spines protruding from their scales—yet these have little impact on their overall combat prowess—and combat prowess is the measure by which zyss judge them.

Before their ancient clash with humanity devastated their civilization, serpentfolk were masters of a sprawling underground empire. Their power was shattered and their god Ydersius decapitated (although not quite slain). The cunning, intelligence, and magical abilities of serpentfolk have diminished from their ancient heights, and most are born without these boons. This is partially the result of cruel genetic meddling among serpentfolk—though the ruling class, zyss, are born with an innate spellcasting ability, their blood runs thin, making them susceptible to wounds. Seen as the failures of the serpentfolk's experiments are the aapophs, who are strong but prone to mutation and lack innate spellcasting.

Today, the central realm of the Darklands retains the old name of the serpentfolk empire that once dominated this region—Sekamina. This name is also the source of the serpentfolk's Aklo title, sekmin, which they are often called in ancient texts. Serpentfolk dominion had declined before ghouls, gugs, umbral gnomes, and other forces. Yet their recent ventures have brought them back to a stronger place in the Darklands. Many serpentfolk sleeping in torpor in secluded vaults have awakened.

Zyss serpentfolk tend toward megalomania, with dreams of returning to their place of dominance. Many of their plans hinge on resurrecting Ydersius, their decapitated god. His headless body still thrashes about, mindless, in the Darklands, waiting to be reunited with his lost skull. Serpentfolk numbers are so small that reclaiming their dominance seems a distant dream, especially since their reproduction is slow. Though a parent can birth a dozen young at once, the gestation period lasts up to a decade, and the likelihood that even one will be zyss is low. There's no telling whether a child will be zyss or aapoph, regardless of parentage. A coveted zyss child is just as likely to arise from aapoph parents as from two zyss, and every serpentfolk colony has someone in charge of sorting the young, identifying the earliest signs of magic in them.

```statblock
creature: "Aapoph Serpentfolk"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
