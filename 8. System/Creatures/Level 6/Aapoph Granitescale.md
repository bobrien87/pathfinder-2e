---
type: creature
group: ["Humanoid", "Mutant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Aapoph Granitescale"
level: "6"
rare_01: "Common"
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
    desc: "+13; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: "Aklo, Common, Sakvroth (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +14, Athletics +15, Intimidation +15"
abilityMods: ["+5", "+4", "+4", "-1", "+1", "+1"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Serpentfolk Venom"
    desc: "**Saving Throw** DC 22 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d4 poison damage and [[Enfeebled]] 1 (1 round) <br>  <br> **Stage 2** 2d4 poison damage and enfeebled 1 (1 round)"
armorclass:
  - name: AC
    desc: "24 (22 with shed scales); **Fort** +16, **Ref** +14, **Will** +11"
health:
  - name: HP
    desc: "120; **Resistances** poison 5"
abilities_mid:
  - name: "+2 Status to Will Saves vs. Mental"
    desc: ""
  - name: "Chipping Scales"
    desc: "`pf2:r` **Frequency** once per day <br>  <br> **Trigger** The granitescale is about to take piercing or slashing damage <br>  <br> **Effect** The granitescale twists to take the blow on their hardest scales, which they shed to reduce the incoming force. The granitescale gains resistance 15 to the damage, but their AC is reduced by 2 for 1 day, when the shed scales regrow."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Longspear +17 (`pf2:1`) (reach), **Damage** 1d8+11 piercing"
  - name: "Melee strike"
    desc: "Fangs +17 (`pf2:1`), **Damage** 1d8+11 piercing plus [[Serpentfolk Venom]]"
  - name: "Ranged strike"
    desc: "Javelin +16 (`pf2:1`) (range 30 ft.), **Damage** 1d6+11 piercing"
spellcasting: []
abilities_bot:
  - name: "Rattling Spear"
    desc: "`pf2:1` **Requirements** The granitescale's last action was a successful longspear Strike <br>  <br> **Effect** The granitescale rattles the base of their spear, attempting an Intimidation check to [[Demoralize]] all enemies within 30 feet (compare the check result to the targets' Will DCs individually)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The mutated aapophs dubbed granitescales have bulky frames covered in hard gray plates. These scales offer protection but shed when struck with too much force. Granitescales like to carve their shed scales into small chips and attach them as rattles to their spears.

Many an unsuspecting victim has heard the hiss of a granitescale's rattle too late.

Before their ancient clash with humanity devastated their civilization, serpentfolk were masters of a sprawling underground empire. Their power was shattered and their god Ydersius decapitated (although not quite slain). The cunning, intelligence, and magical abilities of serpentfolk have diminished from their ancient heights, and most are born without these boons. This is partially the result of cruel genetic meddling among serpentfolk—though the ruling class, zyss, are born with an innate spellcasting ability, their blood runs thin, making them susceptible to wounds. Seen as the failures of the serpentfolk's experiments are the aapophs, who are strong but prone to mutation and lack innate spellcasting.

Today, the central realm of the Darklands retains the old name of the serpentfolk empire that once dominated this region—Sekamina. This name is also the source of the serpentfolk's Aklo title, sekmin, which they are often called in ancient texts. Serpentfolk dominion had declined before ghouls, gugs, umbral gnomes, and other forces. Yet their recent ventures have brought them back to a stronger place in the Darklands. Many serpentfolk sleeping in torpor in secluded vaults have awakened.

Zyss serpentfolk tend toward megalomania, with dreams of returning to their place of dominance. Many of their plans hinge on resurrecting Ydersius, their decapitated god. His headless body still thrashes about, mindless, in the Darklands, waiting to be reunited with his lost skull. Serpentfolk numbers are so small that reclaiming their dominance seems a distant dream, especially since their reproduction is slow. Though a parent can birth a dozen young at once, the gestation period lasts up to a decade, and the likelihood that even one will be zyss is low. There's no telling whether a child will be zyss or aapoph, regardless of parentage. A coveted zyss child is just as likely to arise from aapoph parents as from two zyss, and every serpentfolk colony has someone in charge of sorting the young, identifying the earliest signs of magic in them.

```statblock
creature: "Aapoph Granitescale"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
