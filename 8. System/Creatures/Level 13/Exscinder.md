---
type: creature
group: ["Archon", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Exscinder"
level: "13"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Archon"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+25; [[Darkvision]]"
languages: "Aklo, Chthonian, Diabolic, Draconic, Empyrean, Necril, Sakvroth, Utopian (Telepathy 100 feet, Truespeech)"
skills:
  - name: Skills
    desc: "Arcana +24, Intimidation +26, Occultism +24, Religion +27, Society +26, Heaven Lore +26, Library Lore +26"
abilityMods: ["+8", "+6", "+6", "+5", "+8", "+7"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Censorious Lash"
    desc: "When the exscinder hits a creature with a binding chains Strike, that creature must attempt a DC 30 [[Will]] save. On a failure, it's controlled by the exscinder for its frst action on its next turn (or controlled for its entire next turn on a critical failure)."
armorclass:
  - name: AC
    desc: "33; **Fort** +23, **Ref** +21, **Will** +25"
health:
  - name: HP
    desc: "240; **Immunities** fear effects; **Weaknesses** unholy 10; **Resistances** fire 10"
abilities_mid:
  - name: "Archon's Protection"
    desc: "`pf2:r` **Trigger** An enemy damages the archon's ally and both are within 15 feet of the archon <br>  <br> **Effect** The ally gains resistance 15 to all damage against the triggering damage, and the archon can make a Strike against the enemy. <br>  <br> > [!danger] Effect: Archon's Protection"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Binding Chains +27 (`pf2:1`) (disarm, finesse, holy, magical, trip), **Damage** 2d6 fire plus 3d8+11 bludgeoning plus [[Censorious Lash]]"
  - name: "Ranged strike"
    desc: "Blazing Sigil +25 (`pf2:1`) (fire, holy, magical, spirit, range 40 ft.), **Damage** 5d6 fire plus 3d6 spirit"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 33, attack +25<br>**7th** [[Interplanar Teleport]]<br>**5th** [[Divine Immolation]]<br>**4th** [[Rewrite Memory]] (At Will), [[Translocate]] (At Will)<br>**3rd** [[Ring of Truth]]<br>**2nd** [[Invisibility]] (At Will)<br>**1st** [[Heal]] (At Will), [[Light]], [[Message]], [[Sure Strike]]"
abilities_bot:
  - name: "Change Size"
    desc: "`pf2:1` The exscinder changes size to their choice of Huge, Large, Medium, or Small."
  - name: "Temper thy Words"
    desc: "`pf2:1` The exscinder chooses one written text within 120 feet. They don't need to be able to observe the text, but they can't target one that's deliberately [[Concealed]]. The exscinder censors the text, modifying it to their wishes. The text can't be referenced, making it useless for functions like Casting a Spell from a scroll, preparing spells from a spellbook, or consulting a scholarly journal. If the text is attended, the creature possessing it can attempt a DC 33 [[Will]] save; an unattended text automatically gets a critical failure."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Mortals require protection from forbidden knowledge and heretical texts. Anywhere across the planes, an exscinder might arrive to claim, confscate, and destroy the dangerous thoughts within. Considering themselves avatars of the virtue of temperance, exscinders repeat the lesson that the cautious tongue refuses to speak wicked words. Though they pass on these words, it's rare for them to take much note of ordinary mortals. The danger is not necessarily the person who learns, but the evil knowledge itself. It's the weed that grows beyond the words on the page and must be torn out by its roots.

```statblock
creature: "Exscinder"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
