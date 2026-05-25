---
type: creature
group: ["Beast", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Lamia"
level: "6"
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
    desc: "+13; [[Darkvision]]"
languages: "Chthonian, Common"
skills:
  - name: Skills
    desc: "Athletics +16, Deception +15, Diplomacy +11, Intimidation +13, Stealth +15, Survival +11, Cult Lore +11"
abilityMods: ["+6", "+3", "+2", "+1", "+3", "+3"]
abilities_top: []
armorclass:
  - name: AC
    desc: "24; **Fort** +12, **Ref** +15, **Will** +15"
health:
  - name: HP
    desc: "95"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Spear +17 (`pf2:1`), **Damage** 1d6+10 piercing"
  - name: "Melee strike"
    desc: "Tail +16 (`pf2:1`) (agile), **Damage** 1d6+10 bludgeoning plus [[Grab]]"
  - name: "Melee strike"
    desc: "Spear +14 (`pf2:1`) (thrown 10), **Damage** 1d6+10 piercing"
  - name: "Melee strike"
    desc: "Javelin +13 (`pf2:1`) (thrown 30), **Damage** 1d6+10 piercing"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 25, attack +17<br>**4th** [[Suggestion]]<br>**2nd** [[Blur]], [[Humanoid Form]] (At Will)<br>**1st** [[Charm]], [[Illusory Disguise]] (At Will), [[Illusory Object]] (At Will), [[Sleep]], [[Ventriloquism]] (At Will)"
abilities_bot:
  - name: "Lamia's Caress"
    desc: "`pf2:2` The lamia touches a creature, who must succeed at a DC 23 [[Will]] save or become [[Stupefied 1]]. If the target fails additional saves against this ability, the condition value increases by 1 (to a maximum of [[Stupefied 4]]). This condition value decreases by 1 every 24 hours."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Just as they were cursed long ago, lamias can inflict a curse on those they touch, clouding the victim's mind and pushing conscious thought toward animalistic instincts. Creatures affected by this curse grow reckless, becoming unaware of the consequences of their own actions. This makes the hapless victim all the more susceptible to the lamia's cunning illusions and insidious charms. The lamia's animalistic nature and the effect of their cursed touch have led some scholars to theorize that the original lamias must have, millennia ago, turned away from their own reason and intellect and embraced the life of simple beasts. Whether this change was rewarded as a monstrous gift from Lamashtu or inflicted as a curse for abandoning their responsibilities by Pharasma, remains a subject of debate to this day.

Whatever the source of this ancient transformation, lamias have grown to enjoy the strengths it has granted them. They continue to cling to a hatred of the gods, seeing them as the cause of their eternal exile from the societies they watch with jealous eyes while hidden amid the ruins of lost civilizations. Because lamias blame divine powers for their curse, they take special delight in the downfall of temples, the suffering and death of divine spellcasters, and the spread of dissension within organized religions.

While they can briefly assume humanoid form with magic, lamias are usually forced to hide from civilization, making their homes in the barren wilderness. There, they attract cults of their own. With the help of these cultists, lamias strive to bring down popular faiths, introduce schisms into flourishing churches, and humiliate or defame high-profile religious leaders. Most lamias have no true religious faith in anything, hearing instead a mystical calling that manifests as sighs on the desert wind or murmurs from the dark places between the stars.

Lamias are traditionally matriarchal, revering the eldest female among them as leader, mother, and shaman.

Lamias are bloodthirsty victims of an ancient curse for which they blame the gods. Most lamias are humanoid from the waist up but have the lower bodies of serpents. Sinister magic comes naturally to a lamia, and they prefer the use of illusions to deceive prey for later consumption, or simply to torture.

```statblock
creature: "Lamia"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
