---
type: creature
group: ["Beast", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Lamia Matriarch"
level: "8"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Beast"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Darkvision]]"
languages: "Chthonian, Common, Draconic"
skills:
  - name: Skills
    desc: "Athletics +18, Deception +20, Diplomacy +20, Intimidation +18, Occultism +17, Stealth +16, Survival +13, Cult Lore +15"
abilityMods: ["+6", "+4", "+3", "+3", "+3", "+6"]
abilities_top: []
armorclass:
  - name: AC
    desc: "27; **Fort** +13, **Ref** +18, **Will** +17"
health:
  - name: HP
    desc: "135; **Immunities** controlled; **Resistances** mental 10"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Scimitar +19 (`pf2:1`) (forceful, sweep), **Damage** 2d6+10 slashing"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 28, attack +20<br>**3rd** (4 slots) [[Enthrall]], [[Haste]], [[Mind Reading]]<br>**2nd** (4 slots) [[Blur]], [[Dispel Magic]], [[Illusory Creature]], [[Invisibility]]<br>**1st** (4 slots) [[Bless]], [[Daze]], [[Detect Magic]], [[Force Barrage]], [[Phantom Pain]], [[Prestidigitation]], [[Read Aura]], [[Soothe]], [[Telekinetic Hand]]"
  - name: "Occult Innate Spells"
    desc: "DC 28, attack +20<br>**4th** [[Suggestion]]<br>**2nd** [[Blur]]<br>**1st** [[Charm]], [[Illusory Disguise]] (At Will), [[Illusory Object]] (At Will), [[Sleep]], [[Ventriloquism]] (At Will)"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The lamia matriarch can take on the appearance of a Medium humanoid. This doesn't change their Speed or their attack and damage modifiers with their Strikes, but it does prevent them from using their cursed touch. Each lamia matriarch has a fixed humanoid form that resembles their upper torso when in their true form. This is the only humanoid form they can adopt using this ability. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Matriarch's Caress"
    desc: "`pf2:2` The lamia matriarch touches a creature, who must succeed at a DC 28 [[Will]] save or become [[Stupefied 2]] ([[Stupefied 4]] on a critical failure). If the target fails additional saves against this ability, the condition value increases by 1 (increases by 2 on a critical failure, to a maximum of [[Stupefied 4]]). This condition value decreases by 1 every 24 hours."
  - name: "Scimitar Storm"
    desc: "`pf2:3` The lamia matriarch makes a scimitar attack against each enemy within reach. Each attack counts toward their multiple attack penalty, but the penalty does not increase until after all the attacks. The first enemy they damage is subject to Matriarch's Caress."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The brilliant and powerful lamia matriarchs possess boundless ambition, always seeking to bring more people and territory into the clutches of their kind. Consequently, they become rulers of other lamia. For all their cruelty toward other creatures, they're fierce protectors of other lamia, and consequently, they quickly come to rule cults or warbands. Regardless of the lamia's gender, these ascended lamias are always known as matriarchs. A lamia matriarch is set apart from their kindred by the occult power they pursue, and some have even had grand designs to break the animalistic curse that transformed them. However, every attempt so far has led to the matriarch's fall.

Lamias are bloodthirsty victims of an ancient curse for which they blame the gods. Most lamias are humanoid from the waist up but have the lower bodies of serpents. Sinister magic comes naturally to a lamia, and they prefer the use of illusions to deceive prey for later consumption, or simply to torture.

```statblock
creature: "Lamia Matriarch"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
