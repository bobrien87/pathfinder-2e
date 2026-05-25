---
type: creature
group: ["Azata", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Yamah"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Azata"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Darkvision]]"
languages: "Diabolic, Draconic, Empyrean (Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +13, Arcana +10, Deception +12, Diplomacy +12, Religion +13, Stealth +13"
abilityMods: ["+3", "+4", "+2", "+3", "+4", "+5"]
abilities_top:
  - name: "Sneak Attack"
    desc: "The creature's Strikes deal an additional 1d6 precision damage to [[Off Guard]] creatures."
  - name: "Starstrike"
    desc: "Any non-magical starknife becomes a *+1 striking returning weapon* while a yamah wields it."
armorclass:
  - name: AC
    desc: "21; **Fort** +9, **Ref** +13, **Will** +13"
health:
  - name: HP
    desc: "75; **Weaknesses** cold iron 5, unholy 5"
abilities_mid:
  - name: "Free Mind"
    desc: "`pf2:r` **Trigger** An ally of the yamah's attempts a saving throw against an efect that has the mental trait <br>  <br> **Effect** The ally's gains a +4 status bonus to the saving throw. If the ally rolls a success, they get a critical success instead."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Starknife +15 (`pf2:1`) (agile, deadly d6, finesse, holy, magical, versatile s), **Damage** 2d4+8 piercing"
  - name: "Melee strike"
    desc: "Starknife +15 (`pf2:1`) (agile, deadly d6, holy, magical, thrown 20, versatile s), **Damage** 2d4+8 piercing"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 21, attack +14<br>**5th** [[Truespeech]] (Constant)<br>**3rd** [[Holy Light]]<br>**2nd** [[Dispel Magic]], [[Invisibility]], [[Sure Footing]]<br>**1st** [[Detect Magic]] (Constant), [[Divine Lance]], [[Heal]]"
abilities_bot:
  - name: "Crystallized Attack"
    desc: "`pf2:0` **Requirements** The yamah has a charged gem on its forceful quartz bracelet <br>  <br> **Effect** The yamah channels the magic from an active gem, causing its starknife to glow with unnatural brightness. Their next starknife Strike before the end of their turn deals an extra 1d6 force damage and increases its thrown range to 60 feet. This drains one of their quartz gems."
  - name: "Steal Magic"
    desc: "`pf2:2` The yamah makes a melee spell attack against a creature under the efects of a spell; a yamah automatically succeeds with this attack against a willing creature. On a success, the yamah's divine touch attempts to counteract the spell (counteract rank 3, counteract modifer +16). A successful counteract siphons the magical energy into one of the gems on its *forceful quartz bracelet*, recharging it."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Yamahs are devoted to protecting others from magic used for evil, particularly the kind that traps souls or controls a creature's free will. They relish taking a malevolent spellcaster's magic and turning it to virtuous purposes.

Yamahs often sport stern countenances but still enjoy moments of joy and whimsy like other azatas. In particular, they revel in lighthearted jokes and cheery songs when appropriate. Once they enter combat, however, their bright dispositions change to one of focus and determination. While fghting enemies of freedom, yamahs tend to attack from a distance, using their fight and ranged skills to harry foes. If a spellcaster is involved, yamahs move to the front line, attempting to intercede between their allies and the spellcaster's magic.

Lunar eclipses and other notable celestial events tend to draw yamahs to the Universe. These azatas appear more often during these events to aid the followers of deities with connections to such events, such as Desna and the empyreal lord Ashava. Tales among these faiths speak of yamahs who ally with worshippers in their endeavors against evil fends. These stories inevitably end with the yamah departing after the task is complete, leaving the mortal worshipper without a word.

```statblock
creature: "Yamah"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
