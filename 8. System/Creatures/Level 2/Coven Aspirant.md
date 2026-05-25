---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Coven Aspirant"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7"
languages: "Common, Fey, Jotun"
skills:
  - name: Skills
    desc: "Deception +7, Intimidation +5, Medicine +5, Occultism +8, Stealth +7, Survival +5"
abilityMods: ["+2", "+1", "+1", "+4", "+1", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "15; **Fort** +7, **Ref** +7, **Will** +9"
health:
  - name: HP
    desc: "35"
abilities_mid:
  - name: "Shared Confidence"
    desc: "When a coven aspirant is within @Template[emanation|distance:30]{30 feet} of at least two allies, they and their allies gain a +1 status bonus to Will saves. <br>  <br> > [!danger] Effect: Shared Confidence"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +8 (`pf2:1`) (agile, versatile s), **Damage** 1d4+4 piercing"
  - name: "Melee strike"
    desc: "Dart +7 (`pf2:1`) (agile, thrown 20), **Damage** 1d4+4 piercing"
  - name: "Melee strike"
    desc: "Fist +8 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning"
spellcasting:
  - name: "Occult Prepared Spells"
    desc: "DC 18, attack +10<br>**1st** (3 slots) [[Fear]], [[Grim Tendrils]], [[Ill Omen]]<br>**Cantrips** [[Daze]], [[Figment]], [[Light]], [[Prestidigitation]], [[Void Warp]]"
  - name: "Witch Hex Spells"
    desc: "DC 18, attack +10<br>**1st** [[Needle of Vengeance]], [[Shroud of Night]]"
abilities_bot:
  - name: "Forge Pact"
    desc: "`pf2:1` The coven aspirant forms a temporary coven with two or more willing creatures within 30 feet, all of whom must be able to cast spells. <br>  <br> Members of the temporary coven can cast [[Charm]], [[Entangling Flora]], and [[Illusory Disguise]] as 2nd-rank occult innate spells at will, using DC 17 or their spellcasting DC, whichever is higher. <br>  <br> The coven is dissolved after 3 rounds or when all but one member is dead, whichever comes first. A creature can be a member of only one temporary coven at a time and can join a temporary coven no more than once per 24 hours."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Only the foolish would bring themselves to the attention of hags, but some aspirants strive to join a hag coven out of a desire for power or companionship.

Hidden secrets and occult powers have an irresistible lure for many. Since the majority of these NPCs are spellcasters, consider using alternative spell lists to adjust their themes.

```statblock
creature: "Coven Aspirant"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
