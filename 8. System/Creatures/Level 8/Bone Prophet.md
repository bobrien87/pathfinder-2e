---
type: creature
group: ["Humanoid", "Serpentfolk"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Bone Prophet"
level: "8"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Serpentfolk"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: "Aklo, Common, Necril, Sakvroth (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Arcana +15, Deception +18, Intimidation +16, Occultism +17, Religion +19, Society +15, Stealth +13"
abilityMods: ["+3", "+3", "+2", "+5", "+5", "+6"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Serpentfolk Venom"
    desc: "**Saving Throw** DC 26 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d4 poison damage and [[Enfeebled]] 1 (1 round) <br>  <br> **Stage 2** 2d4 poison damage and enfeebled 1 (1 round)"
armorclass:
  - name: AC
    desc: "27; **Fort** +14, **Ref** +15, **Will** +19 ; +1 status to all saves vs. magic"
health:
  - name: HP
    desc: "115; **Resistances** poison 10"
abilities_mid:
  - name: "Thin of Blood"
    desc: "Bone Prophets recover slowly from injuries. When they take physical damage from a critical hit, they gain 2d4 persistent,bleed damage. They take a –2 circumstance penalty to flat checks to recover from persistent damage and saving throws against afflictions."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Staff +18 (`pf2:1`) (magical, two hand d8), **Damage** 2d4+9 bludgeoning"
  - name: "Melee strike"
    desc: "Fangs +17 (`pf2:1`) (finesse), **Damage** 2d6+9 piercing plus [[Serpentfolk Venom]]"
spellcasting:
  - name: "Divine Spontaneous Spells"
    desc: "DC 28, attack +20<br>**4th** (3 slots) [[Fly]], [[Read Omens]], [[Talking Corpse]]<br>**3rd** (4 slots) [[Bind Undead]], [[Blindness]], [[Chilling Darkness]], [[Vampiric Feast]]<br>**2nd** (4 slots) [[Blood Vendetta]], [[Darkness]], [[Resist Energy]], [[See the Unseen]]<br>**1st** (4 slots) [[Bane]], [[Command]], [[Detect Magic]], [[Fear]], [[Guidance]], [[Harm]], [[Light]], [[Read Aura]], [[Ventriloquism]], [[Void Warp]]"
  - name: "Occult Innate Spells"
    desc: "DC 28, attack +20<br>**6th** [[Dominate]]<br>**5th** [[Illusory Scene]]<br>**4th** [[Suggestion]]<br>**2nd** [[Blur (Self Only, At Will)]]<br>**1st** [[Illusory Disguise]] (At Will), [[Ventriloquism]] (At Will)"
abilities_bot:
  - name: "Raise Serpent"
    desc: "`pf2:3` **Frequency** once per day <br>  <br> **Effect** The bone prophet animates corpses of snakes, serpentfolk, or similar serpentine creatures within a @Template[emanation|distance:30]. Any flesh on the bodies sloughs off, and they rise as skeletons. The bone prophet can raise one Large creature as a [[Skeletal Giant]] or up to three Medium creatures as Skeletal Champions; the equipment and attacks might be different depending on the corpses' possessions. These skeletons have the minion trait and are under the bone prophet's control; the bone prophet can give all these minions the same command with a single action that has the concentrate trait. Any skeletal minions that still remain after 10 minutes crumble to dust."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The speakers for the dead known as bone prophets hold an esteemed place as voices for their decapitated god. Burial rites, necromantic rituals, and the delivery of cryptic utterances supposedly whispered to them by Ydersius all fall under the dominion of these priests.

Before their ancient clash with humanity devastated their civilization, serpentfolk were masters of a sprawling underground empire. Their power was shattered and their god Ydersius decapitated (although not quite slain). The cunning, intelligence, and magical abilities of serpentfolk have diminished from their ancient heights, and most are born without these boons. This is partially the result of cruel genetic meddling among serpentfolk—though the ruling class, zyss, are born with an innate spellcasting ability, their blood runs thin, making them susceptible to wounds. Seen as the failures of the serpentfolk's experiments are the aapophs, who are strong but prone to mutation and lack innate spellcasting.

Today, the central realm of the Darklands retains the old name of the serpentfolk empire that once dominated this region—Sekamina. This name is also the source of the serpentfolk's Aklo title, sekmin, which they are often called in ancient texts. Serpentfolk dominion had declined before ghouls, gugs, umbral gnomes, and other forces. Yet their recent ventures have brought them back to a stronger place in the Darklands. Many serpentfolk sleeping in torpor in secluded vaults have awakened.

Zyss serpentfolk tend toward megalomania, with dreams of returning to their place of dominance. Many of their plans hinge on resurrecting Ydersius, their decapitated god. His headless body still thrashes about, mindless, in the Darklands, waiting to be reunited with his lost skull. Serpentfolk numbers are so small that reclaiming their dominance seems a distant dream, especially since their reproduction is slow. Though a parent can birth a dozen young at once, the gestation period lasts up to a decade, and the likelihood that even one will be zyss is low. There's no telling whether a child will be zyss or aapoph, regardless of parentage. A coveted zyss child is just as likely to arise from aapoph parents as from two zyss, and every serpentfolk colony has someone in charge of sorting the young, identifying the earliest signs of magic in them.

```statblock
creature: "Bone Prophet"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
