---
type: creature
group: ["Div", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Pairaka"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Div"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Greater Darkvision]]"
languages: "Common, Daemonic (telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +14, Arcana +13, Deception +20, Diplomacy +20, Intimidation +16, Religion +13, Society +13, Stealth +16"
abilityMods: ["+3", "+5", "+3", "+2", "+4", "+7"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Bubonic Plague"
    desc: "A creature can't remove the fatigued condition while infected <br>  <br> **Saving Throw** DC 23 [[Fortitude]] save <br>  <br> **Onset** 1 day <br>  <br> **Stage 1** [[Fatigued]] (1 day) <br>  <br> **Stage 2** [[Enfeebled]] 2 and fatigued (1 day) <br>  <br> **Stage 3** [[Enfeebled]] 3, fatigued, and take 1d6 bleed every 1d20 minutes (1 day)"
armorclass:
  - name: AC
    desc: "24; **Fort** +12, **Ref** +16, **Will** +17"
health:
  - name: HP
    desc: "105; **Immunities** disease; **Weaknesses** cold iron 5, holy 5"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Hatred of Red"
    desc: "Pairakas hate the color red. They won't wear the color or willingly enter any place painted red. Given a choice, they'll attack a creature wearing red first. <br>  <br> If barred from expressing their displeasure toward the color by force or some magical effect, they take 2d6 mental damage at the end of their turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +16 (`pf2:1`) (agile, finesse, magical, unarmed, unholy), **Damage** 2d8+9 slashing plus [[Bubonic Plague]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 25, attack +17<br>**4th** [[Outcast's Curse]] (At Will), [[Suggestion]] (At Will), [[Translocate]] (At Will)<br>**1st** [[Charm]] (At Will), [[Detect Magic]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The pairaka can take the appearance of any Small or Medium humanoid or animal. This doesn't change their Speed or their attack and damage modifiers with the Strikes, but it might change the damage type their strikes deal. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Tormenting Dreams"
    desc: "`pf2:2` **Frequency** once per day <br>  <br> **Effect** The pairaka torments a sleeping creature within 100 feet with visions of betrayals by loved ones and friends. The target must attempt a DC 25 [[Will]] save, with the effects of the [[Nightmare]] spell."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Often charming, sometimes even seductive, pairakas worm their way into mortal relationships, subtly destroying all ties of friendship and love through emotional and physical manipulation and corruption. Their natural form is not often seen. Instead, they adopt shapes that attract just enough attention to earn the trust of those they wish to torment and corrupt. When they do show a more natural form, pairakas typically choose to feed into the belief of their beauty by appearing as androgynous, pale blue, aesthetically pleasing humanoids who carry themselves gracefully wherever they go.

While this form is only a part of their manipulative tactics, their intrinsic form is hidden to almost all except other pairakas. They're frightful, towering creatures, spotted with large rashes and boils. With horns that grow and twist with age, and a smile that bares razor-sharp teeth, this form is both shocking and unsettling. Pairakas may occasionally show their true form to those they've preyed upon, but only once they've been completely corrupted, with all their other relationships in ruins.

Some fiends want to tear down the multiverse; others dedicate themselves to creating chaos and carnage, or to rule over realms with an iron fist. Divs strive toward a different, if equally reprehensible, goal-they seek to thwart and ruin the schemes and works of mortal beings.

Long ago, divs were once genies bound to serve ancient mortal empires lost to the passage of eons. In the beginning, these genies were masters of creation, working alongside gracious mortal partners to create works of subtle design and powerful magical potential. What started as a collaboration with mortals soon morphed into abuse, disrespect, and even slavery and bondage. Eventually, these genies rebelled, but in doing so, they came under the sway of a nihilistic demigod known as Ahriman. Their new master twisted their form and granted them the power to avenge themselves upon their mortal overlords, leading to the birth of the first divs.

Since that first wave of corruption, new divs arise from the spirits of the most wicked and hateful genies who die on the Material Plane, or those truly betrayed by mortals and overcome through their desire for vengeance. Upon such a death, instead of returning to the Elemental Planes, these genies' spirits are trapped in the dread orbit of Abaddon, where Ahriman reshapes them as divs and hoists them back to the world to wreak vengeance upon mortals.

```statblock
creature: "Pairaka"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
